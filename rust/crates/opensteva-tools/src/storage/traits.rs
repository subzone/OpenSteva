//! MemoryBackend trait for all storage backends.

use opensteva_core::{OpenStevaError, RetrievalResult};
use serde_json::Value;

pub trait MemoryBackend: Send + Sync {
    fn backend_id(&self) -> &str;
    fn store(
        &self,
        content: &str,
        source: &str,
        metadata: Option<&Value>,
    ) -> Result<String, OpenStevaError>;
    fn retrieve(
        &self,
        query: &str,
        top_k: usize,
    ) -> Result<Vec<RetrievalResult>, OpenStevaError>;
    fn delete(&self, doc_id: &str) -> Result<bool, OpenStevaError>;
    fn clear(&self) -> Result<(), OpenStevaError>;
    fn count(&self) -> Result<usize, OpenStevaError>;
}
